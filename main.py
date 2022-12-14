import heapq

# using existing libraries 
def convertMax(maxHeap):
  # Write your code here
  heapq.heapify(maxHeap)
  return maxHeap
  #print(maxHeap)
  


#print(convertMax([9, 4, 7, 1, -2, 6, 5]))

def min_heapify(heap, idx):
  print("MIN HEAPIFYING for: ", heap, idx, heap[idx])
  l = (idx*2) + 1
  r = (idx*2) + 2
  smallest_idx = idx
  smallest_num = heap[idx]
  if l < len(heap) and heap[l] < smallest_num:
    smallest_num = heap[l]
    smallest_idx = l
  if r < len(heap) and heap[r] < smallest_num:
    smallest_num = heap[r]
    smallest_idx = r
  if smallest_idx != idx:
    # swap to make min heap
    tmp = heap[idx]
    heap[idx] = smallest_num
    heap[smallest_idx] = tmp

    # re-heapify subtree after swap
    # new element at smallest_idx needs to satisfy invariant
    min_heapify(heap, smallest_idx)
      

# using existing libraries 
def convertMax_raw(maxHeap):

  # for all internal nodes, call min_heapify
  # internal nodes range from 0 to N/2
  for i in range((len(maxHeap)//2)-1, -1, -1):
    min_heapify(maxHeap, i)
  return maxHeap
  #print(maxHeap)


print(convertMax_raw([9, 4, 7, 1, -2, 6, 5]))