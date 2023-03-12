class ResponseMessagesValues:
    USER_SUCCESSFULLY_CREATED = "El usuario fue creado exitosamente."
    USER_ALREADY_EXIST = "El usuario ya existe."
    OBJECT_ALREADY_EXIST = "Ya existe un objeto con este ID."
    OBJECT_NOT_FOUND = "El objeto no fue encontrado."
    MISSING_USER_MODEL_INFO = "La información suministrada no es suficiente realizar ésta acción."
    BD_CONNECTION_ISSUE = "Ha ocurrido un error al intentar interactuar con la base de datos."
    CACHING_CONNECTION_ISSUE = "Ha ocurrido un error al intentar interactuar con el servicio de cache."
    PASSWORD_MISSMATCH = "Las contraseñas no coinciden."
    NOT_ALLOWED = "No está autorizado para realizar ésta acción"
    NOT_VERIFIED = "El usuario no está verificado"
    NOT_ENABLED = "El usuario no está activo. " \
                  "Comuníquese con el administrador del sistema para activarlo en caso de requerirlo."
    CANNOT_DOWNGRADE_ADMIN_ROLE = "No se pueden reducir los permisos de los usuarios administradores"
    TOKEN_EXPIRED = "El token ha expirado."
    INVALID_TOKEN = "El token es invalido"
    VERIFICATION_MESSAGE_SENT = "El mensaje de verificación fue enviado correctamente. " \
                                "En caso de no poder visualizarlo en su bandeja de entrada porfavor espere unos " \
                                "minutos o comuniquese con servicio al cliente"
    USER_VERIFIED = "El usuario fue verificado exitosamente"
    NO_MATCHING_HATCH = "No se proporcionó el hash o el mismo no coincide con el cuerpo del mensaje"
    INVALID_ENCRYPTION_KEY = "La llave de verificación del cuerpo no es valida"
    GENERAL_ENCRYPTION_ERROR_MSG = "Ocurrio un error al verificar el cuerpo del mensaje"
    GENERAL_REQUESTS_FAILURE_MESSAGE = "El servicio no se encuentra disponible por el momento. Porfavor intente mas tarde."
