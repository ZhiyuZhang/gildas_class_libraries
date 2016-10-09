Function hanning, input
;  Hanning smooth three (chnanels)
;  USEAGE
;  output = hanning(input)
channels =  n_elements(input) -1 
print,   channels
arrayy      =  input 
arrayl      =  input
arrayr      =  input 
arrayl[2:channels]   = input[1:channels-1]
arrayr[1:channels-1] = input[2:channels]
arrayy               = input  
output = (arrayy/2+arrayl/4+arrayr/4)
return,output 
end 
