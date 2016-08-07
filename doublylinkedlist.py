class DoublyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, data = None):			
		# If adding first node, that first node is both the head and tail:
		if self.head == None:
			self.head = Node(data)
			self.tail = self.head
		# Else set the newly added node to be the tail, change prev and next accordingly:
		else:
			node = Node(data)
			node.prev = self.tail
			self.tail.next = node
			self.tail = node

		# print 'Length of Doubly-Linked List is now: {}'.format(len(self.li))
		return self

	def delete(self, idx):
		node = self.head
		i = 0

		# Iterate starting at head until we find index:		
		while node != None:
			# When index found, set the prev and next nodes to point to each other
			# and ignore the node marked for deletion:
			if i == idx:
				# Edge case - deleting the head:
				if node == self.head:
					node.next.prev = None
					self.head = node.next
				# Edge case - deleting the tail:
				elif node == self.tail:
					node.prev.next = None
					self.tail = node.prev
				# All other cases:
				else:
					node.prev.next = node.next
					node.next.prev = node.prev
				break

			node = node.next
			i += 1

		if node == None:
			print 'Index out of bounds, cannot delete at index {}.'.format(idx)

		return self

	def insertAfter(self, idx, data = None):
		node = self.head
		i = 0

		# Iterate starting at head until we find index:		
		while node != None:
			# When index found, set the head, tail, prev, and next nodes accordingly
			# for the new node and its surrounding nodes:
			if i == idx:
				newNode = Node(data)	
				newNode.prev = node
				# Edge case - inserting after the tail:
				if node == self.tail:
					self.tail = newNode
				# All other cases:
				else:
					newNode.next = node.next
					node.next.prev = newNode					
				node.next = newNode				
				break

			node = node.next
			i += 1

		if node == None:
			print 'Index out of bounds, cannot insert at index {}.'.format(idx)	

		return self				

	def insertBefore(self, idx, data = None):
		node = self.head
		i = 0

		# Iterate starting at head until we find index:		
		while node != None:
			# When index found, set the head, tail, prev, and next nodes accordingly
			# for the new node and its surrounding nodes:
			if i == idx:
				newNode = Node(data)	
				newNode.next = node
				# Edge case - inserting before the head:
				if node == self.head:
					self.head = newNode
				# All other cases:
				else:
					newNode.prev = node.prev
					node.prev.next = newNode
				node.prev = newNode
				break

			node = node.next
			i += 1

		if node == None:
			print 'Index out of bounds, cannot insert at index {}.'.format(idx)	

		return self			

	def display(self):
		print 'List content:',

		node = self.head
		while node != None:
			print node.data,
			node = node.next			

		print '\n'	

class Node(object):
	def __init__(self, data):
		self.prev = None
		self.next = None
		self.data = data

print 'Creating Doubly-Linked List...'
dll = DoublyLinkedList()

print
print 'Adding node with data: \'This\''
dll.add('This').display()
print 'Adding node with data: \'is\''
dll.add('is').display()
print 'Adding node with data: \'a\''
dll.add('a').display()
print 'Adding node with data: \'doubly\''
dll.add('doubly').display()
print 'Adding node with data: \'linked\''
dll.add('linked').display()
print 'Adding node with data: \'list\''
dll.add('list.').display()

print 'Deleting first node (head) (index 0)'
dll.delete(0).display()
print 'Deleting thirf node (index 2)'
dll.delete(2).display()
print 'Deleting third node again (index 2)'
dll.delete(2).display()

print 'Inserting \'That\' before first node (head) (index 0)'
dll.insertBefore(0, 'That').display()

print 'Inserting \'doubly-linked\' after third node (index 2)'
dll.insertAfter(2, 'doubly-linked').display()

print 'Head is:', dll.head.data
print 'Tail is:', dll.tail.data
print 'Next of head is:', dll.head.next.data
print 'Prev of tail is:', dll.tail.prev.data

# arr = ['a', 'b', 'c']
# arr.insert(-6, 'd')
# print arr