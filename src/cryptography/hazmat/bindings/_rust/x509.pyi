import datetime
import typing

from cryptography import x509

def parse_csr_extension(
    der_oid: bytes, ext_data: bytes
) -> x509.ExtensionType: ...
def parse_crl_entry_ext(der_oid: bytes, data: bytes) -> x509.ExtensionType: ...
def parse_crl_extension(
    der_oid: bytes, ext_data: bytes
) -> x509.ExtensionType: ...
def load_pem_x509_certificate(data: bytes) -> x509.Certificate: ...
def load_der_x509_certificate(data: bytes) -> x509.Certificate: ...
def encode_precertificate_signed_certificate_timestamps(
    extension: x509.PrecertificateSignedCertificateTimestamps,
) -> bytes: ...

class Sct: ...
class Certificate: ...
