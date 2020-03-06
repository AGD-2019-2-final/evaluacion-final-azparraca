import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

if __name__ == '__main__':


   
    curkey = None
    total = 0

    
    for line in sys.stdin:

        
        key, val = line.split("\t")
        val = int(val)

        
        if key == curkey:

#la misma clave con los valores acumulados

            total += val

       
        else: 

            
            if curkey is not None:
                #Salida resultado con valores reducidos
               
                sys.stdout.write("{}\t{}\n".format(curkey, total))

           
            curkey = key
            total = val
        
   
    sys.stdout.write("{}\t{}\n".format(curkey, total))