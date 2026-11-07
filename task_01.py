class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  # реверс однозв'язного списку
  def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev # змінюємо напрямок посилання
            prev = current
            current = next_node
        self.head = prev

  # сортування вставками (Insertion Sort)
  def insertion_sort(self):
        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next  # наступний вузол оригінального списку
            
            # Вставка поточного вузла у відсортований список
            if sorted_head is None or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                search_node = sorted_head
                while search_node.next is not None and search_node.next.data < current.data:
                    search_node = search_node.next
                current.next = search_node.next
                search_node.next = current
            
            current = next_node  # Переходимо до наступного елемента

        self.head = sorted_head

  # Об'єднання двох відсортованих однозв'язних списків
  @staticmethod
  def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    temp = Node()
    tail = temp

    p1 = list1.head
    p2 = list2.head

    while p1 is not None and p2 is not None:
        if p1.data <= p2.data:
          tail.next = p1
          p1 = p1.next
        else:
          tail.next = p2
          p2 = p2.next
        tail = tail.next

    if p1 is not None:
        tail.next = p1
    elif p2 is not None:
        tail.next = p2

    merged_list = LinkedList()
    merged_list.head = temp.next
    return merged_list

llist = LinkedList()

for val in [15, 10, 5, 25, 20]:
    llist.insert_at_end(val)

print("Оригінальний список:")
llist.print_list()

llist.reverse()
print("\nРеверсований список:")
llist.print_list()

llist.insertion_sort()
print("\nВідсортований список (сортування вставками):")
llist.print_list()

llist1 = LinkedList()
for val in [2, 7, 12]:
    llist1.insert_at_end(val)

llist2 = LinkedList()
for val in [1, 5, 9, 15]:
    llist2.insert_at_end(val)

print("\nПерший відсортований список:")
llist1.print_list()

print("Другий відсортований список:")
llist2.print_list()

merged = LinkedList.merge_sorted_lists(llist1, llist2)
print("\nОб'єднаний відсортований список:")
merged.print_list()
