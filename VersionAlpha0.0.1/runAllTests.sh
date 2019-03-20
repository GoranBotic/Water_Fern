#This script is used to execute a full and complete test of the system 

nosetests -v Tests.py

cd frontend 
for l in $(find | grep "Tests.py"); do
    nosetests -v $l
done

cd ../backend
for l in $(find | grep "Tests.py"); do 
    nosetests -v $l 
done 
