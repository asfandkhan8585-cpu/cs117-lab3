section .data
  msg1    db 'Addition RESULT: ',0  
  
  msg1Len equ $-msg1 
	
  add_result db 0 

  msg2    db 'Multiplication RESULT: ',0   
  
  msg2Len equ $-msg2 
	
  mul_result db 0 

section .text
  global _start

_start:

   mov al, 4
   mov bl, 2

      add al, 2              
   add al, '0'           
  
   mov [add_result], al

  
  
   mov al, 4 
  
  mul bl   
  
  add al, '0'           
  mov [mul_result], al
  
  mov eax,4
   mov ebx,1
  mov ecx,msg1
   mov edx,msg1Len
  int 0x80

  mov eax,4
  mov ebx,1
   mov ecx,add_result
  mov edx,1
  int 0x80

  mov eax,4
   mov ebx,1
  mov ecx,msg2
   mov edx,msg2Len
  int 0x80

  mov eax,4
  mov ebx,1
  mov ecx,mul_result
  mov edx,1
  int 0x80

  mov eax,1
  mov ebx,0
  int 0x80