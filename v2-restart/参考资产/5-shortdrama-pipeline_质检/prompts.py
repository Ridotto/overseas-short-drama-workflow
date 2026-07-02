from __future__ import annotations

from shortdrama_pipeline.models import CharacterProfile, Shot


def build_script_prompt(
    topic: str,
    duration_seconds: int,
    episode_count: int,
    ratio: str,
    style: str,
    notes: str,
) -> str:
    return f"""
请用中文生成一部短剧的完整生产脚本，输出必须是严格 JSON，不要输出 Markdown。

短剧主题：{topic}
目标总时长：{duration_seconds} 秒
集数：{episode_count}
画幅：{ratio}
风格：{style}
额外要求：{notes or "无"}

JSON 顶层字段必须包含：
- series_title：中文剧名
- series_bible：中文故事设定
- characters：角色列表，每个角色包含 character_id、name、role、age_range、appearance、personality、costume_style、voice_style、consistency_prompt
- episodes：分集列表，每集包含 episode_id、title、duration_seconds、summary、hook、shots

每个 shot 必须包含：
- shot_id
- duration_seconds（每个 shot 的 duration_seconds 必须大于等于 4 且小于等于 10，禁止输出小于 4 秒或超过 10 秒的镜头）
- scene_location
- characters
- visual_description
- dialogue
- camera
- emotion

shot 设计要求：
- 每个 shot 只表达一个核心动作或一个核心情绪推进
- 每个 shot 最多一条关键对白
- dialogue 允许为空，可用动作、表情、反应推进
- 相邻 shot 必须自然承接，便于直接执行为视频分镜

所有创作内容必须是中文。台词要适合中文短剧，节奏快，情绪强，每集结尾有明确钩子。
""".strip()


def build_character_prompt(profile: CharacterProfile) -> str:
    return f"""
请生成中文短剧主体人物定妆照。

角色名：{profile.name}
角色定位：{profile.role}
年龄段：{profile.age_range}
外貌：{profile.appearance}
性格气质：{profile.personality}
服装风格：{profile.costume_style}
台词气质：{profile.voice_style}
一致性要求：{profile.consistency_prompt}

画面要求：单人主体，正面或三分之二侧面，五官清晰，服装完整，真实影视质感，适合后续作为视频参考图。
不要生成文字、水印、多人合照、夸张漫画风。
""".strip()


def build_seedance_prompt(
    series_title: str,
    episode_number: int,
    shot_number: int,
    shot: Shot,
    style: str,
) -> str:
    dialogue = " / ".join(shot.dialogue) if shot.dialogue else "无，可用动作和表情推进。"
    return f"""
请用中文生成短剧镜头视频提示词，信息精简，突出单一重点。

短剧《{series_title}》第 {episode_number} 集第 {shot_number} 镜头
核心动作：{shot.visual_description}
主情绪：{shot.emotion}
可选关键台词：{dialogue}
主镜头语言：{shot.camera}；整体风格参考 {style}
场景地点：{shot.scene_location}
人物一致性：女主沿用参考图1，男主沿用参考图2，保持同一演员脸型、五官、发型、年龄感、服装风格和人物气质，不要生成明显不同的新演员。
""".strip()
