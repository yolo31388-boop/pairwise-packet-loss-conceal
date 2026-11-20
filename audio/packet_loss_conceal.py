"""第 63 批：地铁里听语音，列车进站时声音变成金属嗡鸣，丢一个包后整句重复，蓝..."""


def pitch_period(samples, rate):
    """基音检测：由基音频率（Hz）求基音周期（采样点数）。"""
    return rate // samples


def frame_len(rate, ms):
    """帧长适配：按采样率和帧长（毫秒）计算每帧采样点数。"""
    return rate * ms // 1000


def plc_delay(codec_delay, jitter):
    """解码延迟：PLC 对齐延迟 = 解码器延迟 + 抖动缓冲深度。"""
    return codec_delay + jitter


def fec_cover(head, total):
    """FEC 范围：前向纠错实际保护的帧占比。"""
    return head / total


def comfort_noise(energy, gain):
    """舒适噪声：DTX 静音期按背景能量和增益生成舒适噪声。"""
    return energy * gain


def reset_state(switch, state):
    """状态重置：采样率/流切换后清空 PLC 状态（旧基音不得延续）。"""
    if switch:
        return None
    return state


def transient_guard(is_transient, repeat):
    """瞬态保护：瞬态（鼓点/爆破音）丢包禁止按周期复制。"""
    if is_transient:
        return False
    return repeat


def fade_gain(index, total):
    """单次淡化：隐藏帧只做一次淡出，index=0 时增益为 1。"""
    return 1.0 - index / total


def clock_drift(local, remote):
    """时钟跟踪：收发两端采样时钟的漂移量（用于抖动缓冲再平衡）。"""
    return local - remote


def device_delay(old, new):
    """设备延迟：蓝牙等设备切换后输出延迟的变化量。"""
    return new - old


def stereo_sync(left, right):
    """双声道同步：左右声道统一隐藏位置，取共同中点避免相位不一致。"""
    return (left + right) // 2


def max_conceal(lost, limit):
    """隐藏上限：连续丢包隐藏帧数不超过上限。"""
    return min(lost, limit)


def recover_fade(frame, total):
    """恢复淡入：丢包恢复后第一帧起线性淡入。"""
    return frame / total


def plc_energy(last, decay):
    """隐藏能量：连续隐藏时能量按衰减系数逐帧递减。"""
    return last * decay


def frame_align(timestamp, frame):
    """帧对齐：时间戳对帧长取模，得到帧内偏移。"""
    return timestamp % frame
