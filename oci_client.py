import os, logging
import oci

logger = logging.getLogger(__name__)

## ~/.oci/config は固定
## OCI_CONFIG_PROFILE でプロファイルを指定可能
def get_config_and_signer(file_location=None, profile_name=None):
    config = {}
    signer = None
    default_profile_name = os.environ.get('OCI_CONFIG_PROFILE') if 'OCI_CONFIG_PROFILE' in os.environ else 'DEFAULT'
    file_loc = '~/.oci/config' if not file_location else file_location
    if os.path.isfile(os.path.expanduser(file_loc)):
        profile = profile_name if profile_name else default_profile_name
        config = oci.config.from_file(os.path.expanduser(file_loc), profile)
        logger.info(f'Using config {file_loc} with profile "{profile}"')
    else:
        if 'OCI_RESOURCE_PRINCIPAL_VERSION' in os.environ:
            ver = os.environ['OCI_RESOURCE_PRINCIPAL_VERSION']
            logger.info(f'Using resource principal signer - OCI_RESOURCE_PRINCIPAL_VERSION={ver}')
            signer = oci.auth.signers.get_resource_principals_signer()
        else:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            logger.info('Using instance principal signer.')
    return (config, signer)

def get(clazz: type):
    config, signer = get_config_and_signer()
    return clazz(config) if not signer else clazz(config, signer=signer)
