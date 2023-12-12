import jwt


class Token:

    @staticmethod
    def encode(
            lang: str,
            secret: str,
            algorithm: str,
            first_name="Q",
            last_name= "A",
            email= "q.a@siteground.com",
            domain="",
            exp=19701250772
    ) -> str:
        """
        Utility method to encode JWT
        :param lang:  Language for the token
        :param secret: Secret for the encoding
        :param algorithm: Encoding algorithm
        :param first_name: First name
        :param last_name: Last name
        :param email: email
        :param domain: valid domain name
        :param exp: expiration in UNIX format
        :return: encoded payload as a string
        """
        encoded = jwt.encode({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "domain": domain,
            "lang": lang,
            "exp": exp
        },
            secret,
            algorithm=algorithm
        )

        return encoded
