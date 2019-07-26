# Questions && Answers

1. What is the runtime complexity of your ring buffer's `append` method?

   O(1) - Constant time for the append, and only one append will occur no matter how large the capacity of the buffer is.

2. What is the space complexity of your ring buffer's `append` function?
   O(1) - Constant space because no new variables are allocated at any point of the methods execution - the self.current is already allocated and reassigned, and the list is a fixed length array that does not get reallocated and only its items are reassigned by reference.

3. What is the runtime complexity of your ring buffer's `get` method?
   O(n) - The filter method has to iterate through the entire list once to compare against the conditional. As the capacity of the buffer increases by 1, the amount of items that need to be checked increases by 1 so this would indicate a linear time complexity. I plan to get this to constant time by first converting the list to a set, which requires all values to be unique, thus leaving one None value at the end of the list, since all None values that have to be removed are going to occur only before the entire list is filled once and at that point they will all occur starting at the +1 position of the index of the last value to be appended and then continue to the end of the list. Then, after converting to a set, a constant time pop operation could be carried out to pop the last None out of the list.

4. What is the space complexity of your ring buffer's `get` method?

   Currently, I think it is possibly constant space, I don't imagine the argument, x, to the lambda function is allocated for ever item in the list as the callback executes, but I'm not really sure and will continue to research what is going on under the hood here. However, at worst case it could possible be linear time complexity if one assumes that x is allocated once for every item in the buffer. However, considering the refactor with the set mentioned above, I believe then it can be brought to worst case constant space since a new variable does not have to be reallocated in order to reassign the list as a set and then pop out the last None.

5. What is the runtime complexity of the provided code in `names.py`?
   O(n2) - quadratic time - the first loop is O(n) which then also has a loop in it that is also O(n), therefore, as n increases each list increases the amount of operations by n \* n. The appending step in the last is going to be constant time regardless of the size of n since the item is being added to the end of the array and there is no need to reallocate the referenced items prior.

6. What is the space complexity of the provided code in `names.py`?

   The space complexity is at best O(1) ...but, I'd imagine that each appending actually would need to reallocate space, even though python has dynamically sizing arrays, as the list grows increases by 1, 1 bit in memory needs to be occupied, so techically as n increases + 1 , the need for 1 more space to put that value does exist, so this is probably at worst - linear space complexity.

7. What is the runtime complexity of your optimized code in `names.py`?
   O(n) - the for loop is the key determining factor for the overall time complexity here.
8. What is the space complexity of your optimized code in `names.py`?

   O(1) - no new variables are allocated in any loop or recursive process involving the input size.
