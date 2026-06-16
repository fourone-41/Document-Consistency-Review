import json
import sys
import re

filepath = r"C:\Users\EDY\.cursor\projects\d\agent-transcripts\5bf54d01-df46-4550-bf5d-9c721eaffd1c\5bf54d01-df46-4550-bf5d-9c721eaffd1c.jsonl"

user_messages = []
assistant_key_messages = []

with open(filepath, 'r', encoding='utf-8') as f:
    for line_num, line in enumerate(f, 1):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        
        role = obj.get('role', '')
        content_list = obj.get('message', {}).get('content', [])
        
        text_parts = []
        for item in content_list:
            if item.get('type') == 'text':
                text_parts.append(item.get('text', ''))
        
        full_text = '\n'.join(text_parts)
        
        if role == 'user':
            # Extract user_query content
            query_match = re.search(r'<user_query>\s*(.*?)\s*</user_query>', full_text, re.DOTALL)
            if query_match:
                user_messages.append((line_num, query_match.group(1).strip()))
            elif len(full_text) < 5000:  # Short user messages without tags
                user_messages.append((line_num, full_text[:2000]))
        
        elif role == 'assistant':
            # Only keep assistant messages with substantial text (not just tool calls)
            if len(full_text) > 100:
                # Check for key content: code, error fixes, design decisions
                has_code = '```' in full_text
                has_error = 'error' in full_text.lower() or '错误' in full_text or 'Error' in full_text
                has_design = any(kw in full_text for kw in ['方案', '架构', '设计', 'prompt', 'template', 'schema', '数据结构'])
                if has_code or has_error or has_design:
                    assistant_key_messages.append((line_num, full_text[:3000]))

print(f"=== TOTAL USER MESSAGES: {len(user_messages)} ===")
print(f"=== TOTAL KEY ASSISTANT MESSAGES: {len(assistant_key_messages)} ===")
print("\n" + "="*80)
print("USER MESSAGES (with line numbers)")
print("="*80)

for line_num, msg in user_messages:
    print(f"\n--- [Line {line_num}] ---")
    print(msg[:2000])
    print()

# Write assistant messages to a separate file due to size
with open(r"d:\项目文档一致性审查\assistant_key_msgs.txt", 'w', encoding='utf-8') as f:
    for line_num, msg in assistant_key_messages:
        f.write(f"\n--- [Line {line_num}] ---\n")
        f.write(msg[:3000])
        f.write("\n")

print(f"\nAssistant key messages written to assistant_key_msgs.txt ({len(assistant_key_messages)} messages)")
