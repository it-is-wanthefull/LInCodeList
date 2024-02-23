class ListNode:
    def __init__(self, val='0', next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

t = int(input().strip())

for i in range(t):
    command = input().strip()
    current_node = head = ListNode()

    for j in range(len(command)):
        if command[j] == '<':
            if current_node.prev:
                current_node = current_node.prev
        elif command[j] == '>':
            if current_node.next:
                current_node = current_node.next
        elif command[j] == '-':
            if current_node is head:
                continue
            if current_node.next and current_node.prev:
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
                current_node = current_node.prev
            elif not current_node.next and current_node.prev:
                current_node.prev.next = None
                current_node = current_node.prev
            elif current_node.next and not current_node.prev:
                current_node.next.prev = None
        else:  # 그외문자 즉 password
            new_node = ListNode(val=command[j])
            if current_node.next:
                current_node.next.prev = new_node
                new_node.next = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            current_node = new_node

    current_node = head.next
    while current_node:
        print(current_node.val, end='')
        current_node = current_node.next
    print()