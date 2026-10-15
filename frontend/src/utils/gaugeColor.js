export function clamp(value, min = 0, max = 100) {
  return Math.min(max, Math.max(min, value))
}

export function getUsageColor(value) {
  const v = clamp(value)
  const hue = 120 - (v * 1.2) // 120=verde -> 0=rojo
  return `hsl(${hue} 85% 50%)`
}