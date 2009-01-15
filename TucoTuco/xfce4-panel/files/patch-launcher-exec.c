--- ./plugins/launcher/launcher-exec.c.orig	2009-01-12 22:35:30.000000000 +0100
+++ ./plugins/launcher/launcher-exec.c	2009-01-15 20:27:13.000000000 +0100
@@ -49,6 +49,13 @@
 #define WAIT_ANY (-1)
 #endif
 
+#ifdef __APPLE__
+#include <crt_externs.h>
+#define environ (*_NSGetEnviron())
+#else
+extern char **environ;
+#endif
+
 #include "launcher.h"
 #include "launcher-exec.h"
 
