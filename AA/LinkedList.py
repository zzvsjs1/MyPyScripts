from collections import abc


class ListNode:

    def __init__(self, value=None):
        self.prev = None
        self.next = None
        self.value = value

    def swap(self, other: 'ListNode'):
        self.prev, other.prev = other.prev, self.prev
        self.next, other.next = other.next, self.next
        self.value, other.value = other.value, self.value

    def reverse_after(self):
        start: 'ListNode' = self
        while start != self:
            start.next, start.prev = start.prev, start.next
            start = start.prev

    def hook(self, first: 'ListNode', last: 'ListNode'):
        first.prev.next = last.next
        last.next.prev = first.prev

        next = self.next
        self.next.prev = last
        last.next = self.next
        self.next = first
        first.prev = self

    def un_hook(self):
        self.next.prev = self.prev
        self.prev.next = self.next

    @staticmethod
    def create_header() -> 'ListNode':
        new_node = ListNode()
        new_node.prev = new_node
        new_node.next = new_node
        return new_node


class LinkList:
    size: int
    header: ListNode

    def __init__(self, *args):
        self.header: ListNode = ListNode.create_header()
        self.size: int = 0

        if len(args) == 1 and isinstance(args[0], abc.Iterable):
            for i in args[0]:
                self.push_back(i)
        elif len(args) > 1:
            raise ValueError('Too many arguments.')

    def push_back(self, value):
        new_node = ListNode(value)
        new_node.prev = self.header.prev
        new_node.next = self.header

        self.header.prev.next = new_node
        self.header.prev = new_node
        self.size += 1

    def front(self) -> ListNode:
        if self.empty():
            raise ValueError('The list is empty.')

        return self.header.next.value

    def back(self) -> ListNode:
        if self.empty():
            raise ValueError('The list is empty.')

        return self.header.prev.value

    def pop_front(self):
        if self.empty():
            raise ValueError('The list is empty.')

        to_delete: ListNode = self.header.next
        to_delete.next.prev = self.header
        self.header.next = to_delete.next
        self.size -= 1

    def pop_back(self):
        if self.empty():
            raise ValueError('The list is empty.')

        to_delete: ListNode = self.header.prev
        to_delete.prev.next = self.header
        self.header.prev = to_delete.prev
        self.size -= 1

    def empty(self) -> bool:
        return self.size == 0

    def size(self) -> int:
        return self.size

    def swap(self, other: 'LinkList'):
        self.header, other.header = other.header, self.header

    def reverse(self):
        self.header.reverse_after()

    def remove(self, value):
        head: ListNode = self.header
        cur: ListNode = head.next
        while cur is not head:
            if cur.value == value:
                cur.un_hook()
                self.size -= 1
                return
            cur = cur.next

        raise ValueError('No value in list')

    def remove_if(self, compare) -> int:
        if not callable(compare):
            raise ValueError('compare is not callable')

        count: int = 0
        cur: ListNode = self.header.next
        while cur is not self.header:
            if compare(cur.value):
                cur.un_hook()
                count += 1

            cur = cur.next

        return count

    def add_range(self, iter: abc.Iterable):
        if not isinstance(iter, abc.Iterable):
            raise ValueError('iter is not Iterable')

        for i in iter:
            self.push_back(i)


    def merge(self):
        pass

    def splice(self):
        pass

    def __str__(self):
        if self.empty():
            return '[]'

        str_list = ['[']
        temp = self.header.next
        end = self.header

        while temp.next != end:
            str_list.append(str(temp.value))
            str_list.append(', ')
            temp = temp.next

        str_list.append(str(temp.value) + ']')
        return ''.join(str_list)

    def __len__(self):
        return self.size

    def __iter__(self):
        return LinkListIterator(self.header.next, self.header)

    def __reversed__(self):
        return LinkListReverseIterator(self.header.prev, self.header)

    def __contains__(self, item):
        for e in self:
            if e == item:
                return True

        return False

    def __add__(self, other: 'LinkList'):
        temp = LinkList(self)
        for i in other:
            temp.push_back(i)

        return temp

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, LinkList):
            return False

        if other.size != self.size:
            return False

        for i, j in zip(self, other):
            if i != j:
                return False

        return True

    def __ne__(self, other):
        return not(self == other)

class LinkListIterator:

    def __init__(self, start: ListNode, end: ListNode):
        self.__cur = start
        self.__end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.__cur == self.__end:
            raise StopIteration

        value = self.__cur.value
        self.__cur = self.__cur.next
        return value


class LinkListReverseIterator:

    def __init__(self, start: ListNode, end: ListNode):
        self.__cur = start
        self.__end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.__cur == self.__end:
            raise StopIteration

        value = self.__cur.value
        self.__cur = self.__cur.prev
        return value


if __name__ == '__main__':
    my_list = reversed(LinkList(range(20)))
    print(my_list)