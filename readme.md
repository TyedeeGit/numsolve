<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Numsolve is a game designed for practicing solving number theory problems(and other math problems in the future!) quickly. It consists of several games, listed below.

### Prime Factors
Prime factorize numbers fast! Example session shown below:
```
> play prime_factors
Currently playing: Prime Factors [prime_factors]
Figure out prime factors of a number quickly. Type "generate" or "gen" to start. You will be timed.
>> difficulty
The current difficulty is set to 1
>> generate
Your number is: 360
>> check 2^3 3^2 5^1
Good job! You factorized 360 in 14.12 seconds.
>> difficulty 2
The current difficulty is now set to 2
>> generate
Your number is: 75600
>> check really bad guess
Invalid factors! Try again
>> answer
The prime factorization of 75600 = 2^4 * 3^3 * 5^2 * 7^1
You gave up within 12.01 seconds.
```

### Polynomial Solving
Solve polynomial problems quickly! Example session shown below:
```
> play polysolve
Currently playing: Polynomial Solving [polysolve]
Solve polynomials whose solutions are integers. Use "mode" or "m" to set mode and "difficulty" or "diff" to set difficulty. Type "generate" or "gen" to start. You will be timed.
>> mode get
Current mode is set to: Simon's Favorite Polynomials [default]
Generates a polynomial A*p*q + B*p + C*q - D = 0, where p and q are primes.
>> generate
Problem: 2qp + 3p + 3q - 125 = 0, where q and p are primes. Solutions must be given in reverse order.
>> echo (Ap + C)(Aq + B) = AD + BC
(Ap + C)(Aq + B) = AD + BC
>> echo (2p + 3)(2q + 3) = 2(125) + 3(3)
(2p + 3)(2q + 3) = 2(125) + 3(3)
>> mul 2 125
250
>> add 250 9
259
>> echo (2p + 3)(2q + 3) = 259
(2p + 3)(2q + 3) = 259
>> div 259 7
37
>> echo (2p + 3)(2q + 3) = 7 * 37
(2p + 3)(2q + 3) = 7 * 37
>> echo 2p + 3 = 7
2p + 3 = 7
>> echo p = 2
p = 2
>> echo 2q + 3 = 37
2q + 3 = 37
>> div 34 2
17
>> echo q = 17
q = 17
>> check 17 2
Incorrect answer. Try again.
>> check 2 17
You solved the polynomial in 170.86 seconds!
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/TyedeeGit/numsolve.svg?style=for-the-badge
[contributors-url]: https://github.com/TyedeeGit/numsolve/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TyedeeGit/numsolve.svg?style=for-the-badge
[forks-url]: https://github.com/TyedeeGit/numsolve/network/members
[stars-shield]: https://img.shields.io/github/stars/TyedeeGit/numsolve.svg?style=for-the-badge
[stars-url]: https://github.com/TyedeeGit/numsolve/stargazers
[issues-shield]: https://img.shields.io/github/issues/TyedeeGit/numsolve.svg?style=for-the-badge
[issues-url]: https://github.com/TyedeeGit/numsolve/issues
[license-shield]: https://img.shields.io/github/license/TyedeeGit/numsolve.svg?style=for-the-badge
[license-url]: https://github.com/TyedeeGit/numsolve/blob/master/LICENSE.txt