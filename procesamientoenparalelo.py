#include 
#include 

int main(){
    
    int pid; //IDdelproceso
    FILE *fichero;
    puts("Este es un programa de ejemplo de programa multiproceso");
    
    pid = fork();
    switch(pid){
        case -1:
            fprintf(stderr,"Error al hacer fork");
        break;
        case 0:
            fichero = fopen("hijo.txt","w");
            fprintf(fichero,"Hola soy el hijo");
            fclose(fichero);
            /*while(1==1) {
                 
             }*/ 
        break;
        default:
            fichero = fopen("padre.txt","w");
            fprintf(fichero,"Hola soy el padre y mi hijo tiene el pid %d",pid);
            fclose(fichero);
            /*while(1==1) {
                 
             }*/ 
        break;      
    }   
    return 0;
}
