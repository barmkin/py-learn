import ctypes 
import gc

print("____________________________________") 

message = "This is message #1"

# get the memory address of message  
message_mem_address = id(message) 

print(message)
print(message_mem_address)

# get the value through memory address 
value_from_memory_1 = ctypes.cast(message_mem_address, ctypes.py_object).value 

print("Memory Value - ", value_from_memory_1)

print("____________________________________") 

message = "This is message #2"

# get the memory address of message  
message_mem_address = id(message) 

print(message)
print(message_mem_address)

# get the value through memory address 
value_from_memory_2 = ctypes.cast(message_mem_address, ctypes.py_object).value 

print("Memory Value - ", value_from_memory_2)

print("____________________________________") 

collected = gc.collect()
print("Garbage collector: collected",
          "%d objects." % collected)

# gc does not clean an indirect references variable

print("Memory Value - ", value_from_memory_1)
print("Memory Value - ", value_from_memory_2)
