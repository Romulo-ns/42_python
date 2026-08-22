#include <unistd.h>
#include <stdio.h>

char	*ft_itoa(int nbr)
{
    write(1,"ok",2);
    return("ok");
}

int main(int argc, char **agrv)
{
    if(argc == 2)
        printf("%s",ft_itoa(*agrv[1]));
    write(1,"\n",1);
    return 0;
}