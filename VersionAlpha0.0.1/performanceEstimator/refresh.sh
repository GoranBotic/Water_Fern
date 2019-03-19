rm -r dump
mkdir dump

#this verison of the data set obfuscates the code then compiles and decompiles it 
mkdir dump/generated 
unzip origFiles/generated.zip -d dump/generated/ 
rm -r dump/generated/__MACOSX

#this verison of the data set compiles then decompiles the code with the krakatau decompiler before obfuscation
#this was meant to normalize the code
#mkdir dump/generated_krakatau
#unzip origFiles/generated_krakatau.zip -d dump/generated_krakatau/
#rm -r dump/generated_krakatau/__MACOSX

#this verison of the data set compiles then decompiles the code with the procyon decompiler before obfuscation
#this was meant to normalize the code
#mkdir dump/generated_procyon
#unzip origFiles/generated_procyon.zip -d dump/generated_procyon/
#rm -r dump/generated_procyon/__MACOSX 

#this data set was generated similarlly to the first one, except it uses some code from that gpg encrypted data set we found on that one website
mkdir dump/generated_soco 
unzip origFiles/soco_generated.zip -d dump/generated_soco/ 
rm -r dump/generated_soco/__MACOSX

#delete w/e mess we've made of the training data
rm -r trainData 
mkdir trainData 

#copy over the stuff from generated 
#marking 0_orig as the true original file
path="dump/generated"
for f in $(ls $path); do 
    fldr=$path"/"$f
    orig=$(ls $fldr/0_orig/)
    cp $fldr"/0_orig/"$orig trainData/$f".orig"

    for t in $(ls $fldr); do 
        if [ "$t" != "0_orig" ] 
        then 
            pref=$(echo "$fldr/$t/$orig" | md5sum -)
            cp $fldr"/"$t"/"$orig "trainData/"$f"."${pref::-20}
            
        fi
    done
done

#copy the stuff normalized with krakatau
#all of this code is treated as a duplicate of the true original
path="dump/generated_krakatau"
#for f in $(ls $path); do 
#    fldr=$path"/"$f
#    orig=$(ls $fldr/0_orig/)
#    for t in $(ls $fldr); do 
#        pref=$(echo "$fldr/$t/$orig" | md5sum -)
#        cp $fldr"/"$t"/"$orig "trainData/"$f"."${pref::-20}
#    done
#done

#copy the stuff normalized with procyon
#again all of this is treated as a copy
path="dump/generated_procyon"
#for f in $(ls $path); do 
#    fldr=$path"/"$f
#    orig=$(ls $fldr/0_orig/)
#    for t in $(ls $fldr); do 
#        pref=$(echo "$fldr/$t/$orig" | md5sum -)
#        cp $fldr"/"$t"/"$orig "trainData/"$f"."${pref::-20}
#    done
#done

#copy the stuff from the encrypted dataset, marking the originals as needed
path="dump/generated_soco"
for f in $(ls $path); do 
    fldr=$path"/"$f
    orig=$(ls $fldr/0_orig/)
    cp $fldr"/0_orig/"$orig trainData/$f".orig"

    for t in $(ls $fldr); do 
        if [ "$t" != "0_orig" ] 
        then 
            pref=$(echo "$fldr/$t/$orig" | md5sum -)
            cp $fldr"/"$t"/"$orig "trainData/"$f"."${pref::-30}
            
        fi
    done
done

#get rid of the extracted stuff
rm -r dump 
