#include <unistd.h>

void putchar(char *str)
{
    int i;
    int j;

    i = 0;
    while(str[i] != '\0')
    {
        j = 13;
        if(str[i] >= 'a' && str[i] <= 'z')
        {
            while(j > 0)
            {
                if(str[i] == 'z')
                    str[i] = 'a';
                else
                    str[i]++;
                j--;
            }
            write(1,&str[i],1);
        } 
        else if(str[i] >= 'A' && str[i] <= 'Z')
        {
            while(j > 0)
            {
                if(str[i] == 'Z')
                    str[i] = 'A';
                else
                    str[i]++;
                j--;
            }
            write(1,&str[i],1);
        }
        else
            write(1,&str[i],1);
        i++;
    }
}

int main(int argc, char **argv)
{
    int i;

    i = 1;
    if(argc != 2)
        write(1,"\n",1);
    else
    {
        while(i < argc)
        {
            putchar(argv[i]);
            write(1,"\n",1);
            i++;
        }
    }
    return 0;
}
