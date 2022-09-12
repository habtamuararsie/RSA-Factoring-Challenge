#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
// #include <gmp.h>
#include <sys/types.h>
#include <sys/stat.h>

#define Size 1000000

int sieve(int stat)
{
    bool prime[Size];
    static int primes[Size];
    static int n_primes;
    static int current;

    if (stat == 0)
    {
        n_primes = 0;
        current = 0;
        memset(prime, true, sizeof(prime));

        for (int p= 2; p * p < Size; p++)
            if (prime[p] == true)
                for (int i = p * p; i <= Size; i += p)
                    prime[i] = false;
        
        // Print all prime number
        for (int p = 2; p < Size; p++)
            if (prime[p])
            {
                primes[n_primes] = p;
                n_primes += 1;
            }
    }
    else if (stat == 1)
    {
        current++;
        if (current - 1 < n_primes)
            return (-1);
    }
    else
        current = 0;
}

/**
 * print_factor - prints two factors of num in the followgin format
 * n=p*q, where n is the number and p&q are factors
 * p&q are not necessarly primes
 * @num: the number whose factors are to be printed
 * @fs: File stream to print to
 *Return: the number of characters printed
 */

size_t print_factor(mpz_t num, FILE *fs)
{
    mpz_t i, ans, j, mod;
    size_t printed = 0;
    int prime = 2;

    mpz_init(i);
    mpz_init(mod);
    mpz_init(ans);
    mpz_init(j);

    while (1)
    {
        if (mpz_cmp(i, num) >= 0)
            break;
        if (prime != -1)
        {
            prime = sieve(1);
        //printf()
            if (prime != -1)
                mpz_set_ui(i, prime);          
        }
        mpz_mod (mod, num, i);
        if (mpz_cmp_d(mod, 0) == 0)
        {
            mpz_div(ans, num, i);
            printed += mpz_out_str(fs, 10, num);
            printed += fprintf(fs, "=");
            printed += mpz_out_str(fs, 10, ans);
            printed += fprintf(fs, "*");
            printed += mpz_out_str(fs, 10, i)
            printed += fprintf(fs, "\n");
            return (printed);
        }
    }

}
