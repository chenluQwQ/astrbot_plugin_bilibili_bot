# main.py 修改说明

## 需要修改的地方：第 2330 行

### 修改前（硬编码了"柠弥"）

```python
rec_text = re.sub(r'^(主人|柠弥|亲爱的)[，,\s]*', '', rec_text)
```

### 修改后（动态读 OWNER_NAME 配置）

```python
owner_name = (self.config.get("OWNER_NAME", "") or "").strip()
_name_patterns = ["主人", "亲爱的"] + ([re.escape(owner_name)] if owner_name else [])
rec_text = re.sub(rf'^({"|".join(_name_patterns)})[，,\s]*', '', rec_text)
```

## 原因

原写法只过滤掉"柠弥"，别人部署插件时配置的 OWNER_NAME 不是"柠弥"，
生成的推荐语如果带上 OWNER_NAME 开头就清理不掉，会出现"{别人名字}，..."的奇怪开头。

改成动态读取配置后，无论别人 OWNER_NAME 填什么都能正确清理。
