import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJxFV8fKLE1y/e4/M3LoIbTQYqAWZbosCKGyXd77XXnvbddWry2Q+sJISjIPkRlJkBARJzKyn7+NP3/Xf3zXpnwh/85fP/3PT/x/8q+f+Nf/yn/8xH/8FD8/7Z9+il8/7Z9/ij9+2r/85H/8/Oevv83vtT97X3D++qevvea/v0Pf/uuff34K+RZ8MjMIbv4Q4VkOCEfISFrflgF5PEFfTNuPvLHuvmmsfmQEIGCAlHiw6L1PY23FjCd1Stss2VSA9wcsgQw8R9M+ZwbEsqItn6cBKR00DakE8RMsNQsUybCFSgJRRJREdrK8M0oE8FwET/MeHxBQfOD1QrWzEEGSapETKMBTk0sQWEtxghlT869PQzljJ7uvrpNTJZ2E0AXkpcK9IRk1oU/9m16CPIKdJ1wHBcLjBHPuNeLQGM87PzPmleqP5z49J7U6KLQQxSp96e44hpxnOn13WhyJtL11mUe86Xc1BwPDhSaTM+CmFwOpjeKlESZ72kRf6sSyWRJKM1eDKM/CCDTdQkKCGFOiIlV3UECZ4KPC7lUc5xtq4WaRwxjpm2YgyGZWNErUC3sJKXYIt6W4514EOPb+dlI9GAleYAaCOqT99bJmFqW8CS1Qw0d3HH0Pwo3Phm5xxm32Xw9ZFVz6zvIECcjwkeAO3YY3JCEwMZ4yrWVDXL8OL4EylIt0i+TYLTyTe0MTjKFhyutz7C+rTpB57Wq8DSXl0XA0cntbGse5l1zZQ71QjfLcnRefv2mohJEpl/1S1e91n0rRdIZ33sZQoZeTKuWcumBFKEDRhmmN+54t5fW+p57SbjxaW15fP/JGUOztpwdT170QiE5oq96lue+FxbFHOW9LpOHLZS6//lhWvpIoUFOJz14rXxtYpZ1xJHxyGZc/U7jVFUE8EORPXKtpr8d1DLSq1YuiplEgCP1An5X/8B6pBeFbu6Kw/WiZc7cFUSgNOd9PTgk9eQcBvF27Wm1WK1xu0JASTHxob87exqc6UwWo3noeR4yCmGoAyTszDsQlGTSFKwt7wOWyrmmkh8H8cnd/CH0KCT6tjlAO4MUHCQzkpgwFnQcJy5GPQvW5DzcU2CIrsZg31nlFNZNFb4ZLfqOjttH4/CQpW+RlewAROGLm7LmiKI2Hxaykt3wK1VLKJHSyUpcQFq/EJu00NvalI6+xbKnOrgSqUe1coxJRlF4+eGy8Pm6SfGKEWvljWu4DudGswl7K1+ZyD4LbQwynMi+YRt5aq/ccrDZlqWfvhOqBdgA6KmcDTk50AHMM1oYrxQW0GMsAeqJayMzF1k/2zA0NBAkZAO9rGkwSJbbJITLH8ZChJqftCdaUTMg/USyi7actT8Bn8uatHUcC3lLGwn5VX2boKm2frbg0d3GxIFN8EdH8UarEvKNvNJDyixmi7u6wvBU+yk7osdC12WvldMFk0lKM4nIZ+Df8ebggiOuzSZQ0K7qYgOA82joGPmUsaHkLQwVnMSsNWKjjAiZgHftVOd5GxjAYTnuNVMgNLEvooQq060QIUD+9AbJuS/i1b1dc1UvUHr+6a38ugV03lITUY+DlI+ZOMVrAYEUfeMEWvTeMgNNwfQHZWiB03B6OS8MroX3X6GmwpEG+vFOaa+AQM5L9TPSChG5qY6CGT/FyTfy8M83pE0NCqO2p7kIB+lhWA2Nu3QmGpxoX4Iv6lIpCeXvYZtuNC80g0ZsivdRo5D1xpHAMdpkcy53lIqqyKdX7qah6vOOPKFvTEgfK7l/oABURTKlGVSwdIbXlfAHOhvrM+EIN2XJslv48ySSytFuXiYBjBFSa6aIpl1jgwiyutvl4w8QW7+D6JmxF8zE2BmdtWAuhEN9odXGWW+DgXabP3Ri3LKnMKVQVaHb9Mt5LbqOd1EZZrQLewhtKnDxJ5QoQ+kbwmfr61ZcKJ5L45oX1asRPSaV1NTUOdk8TguPdtlxKcZaiGWAA5813ng6O92OF+j2GDJzofCM+AtN/HcSi4KCku3fZcjHLQ5TIi+tS/hsHcnpBp9gUKKmMX0G7fWngZHFLS4YJgEci5NegxwFWcfutyeeWVNU3WLiZeGMHcZD6Zbm8HZqJro0HjxUo9RYX6ALto4prLUSsHOM/sQkxGNo6Y4rMS0nrzcQ7KuoVg9FIC2zdzVxUGZc5w5fQ2GzV0BfBmIsS6+nzYvYN7UvschRql9bduYGXRbe3g8KHtYep/n38CEck0RAK4KtwF+d+xLWjYlozuXkwT89l5Z9GUtDRrsfMW6lQi1orLpRO6ZjHlbmc271qcpAZe9+8c8u95vUt6NEUdWLTVxi84x+/bxCJpPKNmTt927QzH7d07r9srVKEDF+psciSR+zFx5LWmJ+CBaq+GTWO0aZrOIn1Jo9DrX4i806SHMVfZ3Y3RKV6VIGYLjOzTYC/XKXYz5WTdv35mrfCaJS4nTn1d2TvDcydJ7HtUaNP8DRISPGlEUQ+MDJ+kEMYgm9VrQrlbTGUhyVvrUhN3I+5K935cuvUiiZGS+TQ0SFfvVKJNBNCCSN/A0zHHL1TYSWsO77xIcjO+pyjF43IvDm0aRI9TxceusZMZW3qk1iKED8W4YDPXuS3QJexHwl+R+ljKZDFknDc2Q/y9lwERDZxFmxtS+ClxVekxqmd7h8hkzE+mPWaim21h51BC8lnP51V2mi8Riyo7EBI9Y37vHcXqrRlaEI8/CCkaqstyH5CNPWNj3nVNFn1AZXQ6OBHD6CSLO7SunYkgBkppTSMj+QwYSWnJ5JtF6gpXOoYsD/bHOQ1mNgwk6VEW+FIfVCrW2XfRi1stK5/3tTiEuMtiQlJoWRFmN1oYq9XMOQmYwbh8ZZXuO82S3W5ex05jiz0QyHrJjO3hjbXIYSXJkZWHYAe2jsq0n0icjmwYJUfsgJVuMTvReqlDmO8TXsQZpsAz8DUTiJTkZxIFAEoqzwFJ7GkYBVm1YZ9xwtNAI6RghHq2Jq+H45OedTGhbJttXvITmqprVO+u5uGVjc3LVk431PIqR/bB32mNnZazJ8ynhR4rU5MzWFqILy7VF/sjnEUMi0Rs20qzZ0sApEV6o7ohJkRz8yc7X+rlhUWAuzQDX+F9dKE/n662rk5h2kaIWj3HV71nzBZOxaTiWlb3c3/YIRZByqvZZyENz61X/NhY8HcKHG74k9uvu13ouLCy2hDPctNyBUr5UPQ6KdE+LViC+hoPzUhProSC/7qFeCGar3Cuavr71amsttALziG95sCnRD3Tq/N5VqYl21GKspBMrsYYz507PDpNw1b3QbfOI6p4qGrI5sBu+sDZZhCXb58ttYTJ/IbA8zJeNoIRF5xvCl7EtYjFyb7XTOgSSZIjbj0zOIXghjsKeb4nEy6TWfpqC2wBGk+o2sIY2QvEeUhzOdYq3tw8QUC8EGsIYFesqk7MvjCF+hAgU+cl/DoxGwnpebr+5iXKAtgUIIv36jd2BCfIerH737sLYQF81NtWpjS7xPkyO2cyuTIixJPr4UCwYQAzOnB4LoEycIIgSILwfMlghc9ZgzH/fXvvr3Q/vdfGJJ1q5N+/911PX2T7r81abIVOLr/5Sv2U5Jv+z/9bsWKbBrmtdi2/R9/38HR3yd58dffTdv/w/Zb6Rxfu+u/fJnqH767fxum/OiLf//1W/3HF/711/8Aa8GBsA=="))))