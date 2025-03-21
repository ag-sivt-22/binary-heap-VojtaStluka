from dataclasses import dataclass
from typing import Any

@dataclass
class Element:
    value: Any
    priority: int
 
class BinaryHeap:

    def __init__(self):
        self.heap: list[Element] = []
        
    def push(self,element:Element):
        self.heap.append(element)
        idx=(len(self.heap))-1
        while idx>0:
            idx_rodic = (idx-1) // 2
            rodic = self.heap[idx_rodic] 
            dite = element           
            if rodic.priority > dite.priority:
                self.heap[idx] = rodic
                self.heap[idx_rodic] = dite
            else: 
                break
         

    def pop(self):
        min_element=self.heap[0]
        last_element=self.heap.pop()    #najdeme poslední prvek
        if not self.heap: #Pokud jsme odstranili poslední prvek, vrátíme rovnou
            return min_element
        else:
            self.heap[0]=last_element   #prohodíme do kořene
            idx=0

            while True:
                smallest=idx
                left_child = 2 * idx + 1
                right_child = 2 * idx + 2
                if left_child <= len(self.heap)-1 and self.heap[left_child].priority < self.heap[smallest].priority:    #kontrola min_heap a zároveň kontrola, jestli existuje (v poslední vrstvě být nutně nemusí)
                        smallest = left_child
                if  right_child <= len(self.heap)-1 and self.heap[right_child].priority < self.heap[smallest].priority:
                        smallest = right_child
                if smallest != idx:
                    self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]   #prohození ve vrstvách
                    idx = smallest
                else: 
                    break
            return min_element


    def head(self):
        if not self.heap:
            raise Exception("Heap is empty")
        min_idx = 0
        return self.heap[min_idx]
