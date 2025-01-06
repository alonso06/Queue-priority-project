from collections import deque
from src.domain.entities.priority import Priority
from src.domain.entities.user import User
from src.domain.entities.new_user import User2

init_queue:deque[User] = deque([])
queue_p_high:deque[User] = deque([])
queue_p_medium_low:deque[User] = deque([])

for i in range(1,4):
    print('Seleccione la prioridad de su consulta', end='') 
    user_priority = input(f' {Priority.ALTA.value} {Priority.MEDIA.value} {Priority.BAJA.value} ').capitalize()
    user_priority_enum = Priority(user_priority)
    user = User(id=str(i), priority=user_priority_enum)
    init_queue.append(user)

for i in init_queue:
    if i.priority == Priority.ALTA.value:
        queue_p_high.append(i)
    else:
        queue_p_medium_low.append(i)

print(queue_p_high)
print(queue_p_medium_low)