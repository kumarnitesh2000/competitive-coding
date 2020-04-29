#include <stdio.h>
int f=-1,r=-1,q[5],n_q=3;
int H=0,F=0,n_q_count;
//q is the particular frame
//n_q is the no. of frames
void insert_end(int val)
{
    int i;
    if (f==-1){
        f=0;
        r=0;
        q[f]=val;
        n_q_count+=1;
        
    }
    else if(r==n_q-1){
        printf("Overflow.");
    }
    else{
        
        r=r+1;
        i=r;
        while(i!=0){
            q[i]=q[i-1];
            i=i-1;
        }
        q[f]=val;
        n_q_count+=1;
    }
    printf("Queue at Each Time : ");
    for(i=0;i<n_q_count;i++){
        printf(" %d ",q[i]);
        
    }
    F+=1;
    printf("\n");
    
}

int meet(int val){
    int i=0,count=0;
    for(i=0;i<n_q;i++){
        if (q[i]!=val){
            count+=1;
        }
    }
    if (count==n_q){
        return 0;
        
    }
    else{
        return 1;
    }
    
    
}


int main()
{
int r[20],n,i,j,temp;
printf("Enter the no. of refernce string : ");
scanf("%d",&n);
printf("enter the value of refernce string : ");
for(i=0;i<n;i++){
    scanf("%d",&r[i]);
}



for(i=0;i<n;i++)


{
    
    
    
 if(n_q_count<n_q){
     insert_end(r[i]);
                  }
 else{
             //if no. found 
             if (meet(r[i])){
        
                 temp=q[n_q-1];
                 j=n_q;
                 while(j!=0)
                        {
                            q[j]=q[j-1];
                            j=j-1;
                        }
                        q[0]=temp;
                        H+=1;    
                         }
            else{
                    j=n_q;
                    while(j!=0){
                        q[j]=q[j-1];
                        j=j-1;
                        
                    }
                    q[f]=r[i];
                    
                    
                    F+=1;
                    
                }
                
    printf("Queue at Each Time : ");
    for(j=0;j<n_q;j++){
      printf(" %d ",q[j]);
        
    }
    printf("\n");             
                
    }
    

   
    
    
}

printf("No. of faults are : %d and No. of Hits are %d .",F,H);

    return 0;
}
