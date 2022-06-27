import ldap

from django_auth_ldap.config import LDAPSearch, LDAPSettings

# Default values:
DEFL_BIND_DN = LDAPSettings.defaults["BIND_DN"]
DEFL_BIND_PASSWORD = LDAPSettings.defaults["BIND_PASSWORD"]
DEFL_BIND_AS_AUTHENTICATING_USER = LDAPSettings.defaults["BIND_AS_AUTHENTICATING_USER"]
# not yet in master
DEFL_BIND_DN_TEMPLATE = LDAPSettings.defaults.get("BIND_DN_TEMPLATE", None)
DEFL_USER_DN_TEMPLATE = LDAPSettings.defaults["USER_DN_TEMPLATE"]
DEFL_USER_SEARCH = LDAPSettings.defaults["USER_SEARCH"]

# Configured values
CONF_USER_SEARCH = LDAPSearch("ou=people,o=test", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
CONF_PW = "password"
CONF_BAD_PW = "bad_password"
CONF_BIND_DN = "uid=bob,ou=people,o=test"
CONF_USER_TPL = "uid=%(user)s,ou=people,o=test"
CONF_BIND_TPL = "uid=%(user)s,ou=people,o=test"
CONF_BIND_AS_AUTHENTICATING_USER = True


param_list_with_anon = [
    # (sub_test, bind_dn, bind_pw, bind_aau, bind_dn_tmpl, user_dn_tmpl, user_search, is_user),
    (1001, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1002, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (1003, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, True),
    (1004, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1005, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1006, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (1007, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, True),
    (1008, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1009, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1010, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (1011, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1012, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1013, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1014, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (1015, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1016, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1017, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1018, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1019, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1020, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1021, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1022, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1023, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1024, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1025, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1026, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1027, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1028, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1029, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (1030, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1031, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1032, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1033, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1034, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1035, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1036, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1037, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1038, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1039, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1040, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1041, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1042, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1043, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1044, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1045, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (1046, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1047, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1048, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1049, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1050, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (1051, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, True),
    (1052, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1053, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1054, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (1055, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, True),
    (1056, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1057, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1058, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (1059, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1060, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1061, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1062, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (1063, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1064, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1065, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1066, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1067, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1068, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1069, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1070, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1071, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1072, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1073, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1074, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1075, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1076, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1077, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (1078, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1079, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1080, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1081, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1082, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1083, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1084, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1085, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1086, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1087, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1088, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1089, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1090, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1091, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1092, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1093, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (1094, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1095, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1096, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1097, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1098, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1099, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1100, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1101, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1102, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1103, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1104, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1105, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1106, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1107, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1108, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1109, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (1110, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1111, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1112, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1113, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1114, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1115, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1116, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1117, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1118, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1119, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1120, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (1121, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (1122, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1123, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1124, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (1125, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (1126, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (1127, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (1128, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
]


param_list_non_anon = [
    # (sub_test, bind_dn, bind_pw, bind_aau, bind_dn_tmpl, user_dn_tmpl, user_search, is_user),
    (2001, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2002, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2003, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2004, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2005, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2006, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2007, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2008, DEFL_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2009, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2010, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2011, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2012, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2013, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (2014, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2015, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2016, DEFL_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2017, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2018, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2019, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2020, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2021, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2022, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2023, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2024, DEFL_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2025, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2026, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2027, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2028, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2029, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (2030, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2031, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2032, DEFL_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2033, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2034, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2035, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2036, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2037, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2038, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2039, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2040, CONF_BIND_DN, DEFL_BIND_PASSWORD, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2041, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2042, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2043, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2044, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2045, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (2046, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2047, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2048, CONF_BIND_DN, DEFL_BIND_PASSWORD, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2049, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2050, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (2051, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, True),
    (2052, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2053, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2054, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (2055, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, True),
    (2056, CONF_BIND_DN, CONF_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2057, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2058, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (2059, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2060, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2061, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2062, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, True),
    (2063, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2064, CONF_BIND_DN, CONF_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2065, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2066, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2067, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2068, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2069, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2070, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2071, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2072, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2073, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2074, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2075, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2076, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2077, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (2078, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2079, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2080, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2081, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2082, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2083, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2084, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2085, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2086, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2087, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2088, DEFL_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2089, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2090, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2091, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2092, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2093, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (2094, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2095, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2096, DEFL_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2097, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2098, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2099, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2100, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2101, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2102, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2103, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2104, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2105, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2106, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2107, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2108, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2109, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (2110, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2111, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2112, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2113, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2114, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2115, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2116, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2117, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2118, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2119, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2120, CONF_BIND_DN, CONF_BAD_PW, DEFL_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, False),
    (2121, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    (2122, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2123, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2124, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, DEFL_BIND_DN_TEMPLATE, CONF_USER_TPL, CONF_USER_SEARCH, True),
    (2125, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, DEFL_USER_SEARCH, False),
    # Works now
    (2126, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, DEFL_USER_DN_TEMPLATE, CONF_USER_SEARCH, False),
    (2127, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, DEFL_USER_SEARCH, False),
    (2128, CONF_BIND_DN, CONF_BAD_PW, CONF_BIND_AS_AUTHENTICATING_USER, CONF_BIND_TPL, CONF_USER_TPL, CONF_USER_SEARCH, True),
]

