# -*- coding:utf-8 -*-
# 字典和集合中的元素可以是混合类型，虽然很灵活，对于大型项目来说，有时却是灾难
# 要确定元素类型，可利用类型注解、dataclass来缓解，IDE会提醒，但不强制报错，可通过mypy这类静态检查工具来检查
# pydantic可强制在运行时报错，更加安全，只是需要安装三方包，更重一些

from typing import List, Tuple, Union

# 明确告诉别人，这个列表里只能有 int 或 str
scores: List[Union[int, str]] = [98, "Absence", 85]
scores.append(32.33)
print(scores)

# 明确元组的每一项是什么类型
user_info: Tuple[int, str, float] = (1, "Alice", 9.5)


from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    is_active: bool

# user = User(1, "张三", True) # 比 [1, "张三", True] 安全得多
user = User(1, "张三", 22) # 比 [1, "张三", True] 安全得多
print(user)

from pydantic import BaseModel

class User2(BaseModel):
    id: int
    name: str
    is_active: bool

# 这行在运行时会报错，因为 22 不是 bool
user2 = User2(id=1, name="张三", is_active=22)