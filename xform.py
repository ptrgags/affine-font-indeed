class XForm(object):
    def __init__(self, coeffs):
        """
        Initialize with an array of coefficients
        in the form

        [a c]
        [b d]
        [e f]

        This class will handle the rest
        """
        self.coeffs = self.reformat_coeffs(coeffs)

    def __str__(self):
        """
        Print an XML string for use in a .flame file
        """
        coeff_str = ' '.join('{:.4f}'.format(x) for x in self.coeffs)

        return (
            '<xform weight="0.5" color="0" linear="1" coefs="{}" '
            'opacity="1" name="NAME_ME" />').format(coeff_str)

    @classmethod
    def reformat_coeffs(cls, coeffs):
        """
        Rearrange the coefficients from
        [a c]
        [b d]
        [e f]

        to a list [a, b, c, d, e, f]
        """
        a, c = coeffs[0, :]
        b, d = coeffs[1, :]
        e, f = coeffs[2, :]

        return [a, b, c, d, e, f]