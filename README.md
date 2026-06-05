# Ataque-DHCP-Starvation

 ![](data:image/png;base64,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)

**LABORATORIO DE SEGURIDAD DE REDES**

**DHCP STARVATION**

_Documentación Técnica Profesional_

**Estudiante:**

**Heldry Terrero**

Matrícula: 2025-0719

Materia: Seguridad de Redes

Fecha: Junio 2026

  
  

# Aviso de Uso Responsable

|   |
|---|
|**⚠  AVISO IMPORTANTE — LEA ANTES DE UTILIZAR ESTE MATERIAL**<br><br>Este proyecto fue desarrollado únicamente con fines educativos, académicos<br><br>y de laboratorio controlado, en el marco de la asignatura Seguridad de Redes.<br><br>Los scripts, comandos y técnicas incluidos en este repositorio deben ejecutarse<br><br>SOLAMENTE en entornos propios o autorizados, tales como:<br><br>   • Simuladores: PNetLab, GNS3, EVE-NG<br><br>   • Laboratorios internos de práctica académica<br><br>   • Redes virtuales de prueba bajo supervisión docente<br><br>QUEDA ESTRICTAMENTE PROHIBIDO:<br><br>   • Utilizar este material en redes públicas, corporativas o de terceros<br><br>     sin autorización explícita y por escrito.<br><br>   • Interceptar, alterar o interrumpir comunicaciones ajenas.<br><br>   • Aplicar estas técnicas con fines maliciosos o fraudulentos.<br><br>El uso indebido de estas herramientas puede constituir un delito tipificado<br><br>en las leyes de ciberseguridad y delitos informáticos vigentes.<br><br>El autor de este material no se hace responsable del uso indebido del mismo.|

  
  

# Documentación Técnica — Ataque DHCP Starvation

|**Campo**|**Valor**|
|---|---|
|Estudiante|Heldry Terrero|
|Matrícula|2025-0719|
|Materia|Seguridad de Redes|
|Script|dhcp_starvation.py|
|Fecha|Junio 2026|
|Plataforma|PNetLab — Kali Linux|

  
  

# 1. Objetivo del Laboratorio

Demostrar cómo es posible agotar completamente el pool de IPs de un servidor DHCP legítimo mediante el envío masivo de solicitudes con MACs falsas, causando una denegación de servicio que impide a nuevos clientes obtener conectividad.

# 2. Objetivo del Script

Enviar masivamente paquetes DHCP DISCOVER con MACs de origen aleatorias y únicas, consumiendo todas las entradas disponibles en el pool del servidor DHCP, hasta que no queden IPs para asignar a clientes legítimos.

  
  

# 3. Requisitos

## 3.1 Software

•        Python 3.7 o superior

•        Scapy 2.4.3: sudo apt install python3-scapy

•        Kali Linux con interfaz eth1 conectada al switch

•        Privilegios de root (sudo)

## 3.2 Red

•        Atacante: 20.25.7.100/24 en eth1

•        Víctima: 20.25.7.10/24

•        Gateway/Router: 20.25.7.1/24

•        Red: 20.25.7.0/24

# 4. Parámetros del Script

|**Parámetro**|**Descripción**|**Default**|
|---|---|---|
|-i / --iface|Interfaz de red|Requerido|
|-c / --count|Número de DISCOVERs (0=infinito)|0|
|-d / --delay|Delay entre paquetes en segundos|0.005|
|--wait-ack|Escuchar ACKs para registrar IPs|False|
|-v / --verbose|Mostrar cada paquete enviado|False|

# 5. Cómo se Ejecutó el Script

**Comando utilizado durante la demostración:**

sudo python3 dhcp_starvation.py -i eth1 --wait-ack -v

sudo python3 dhcp_starvation.py -i eth1 -c 254

|   |
|---|
|**Resultado esperado en pantalla**<br><br>[*] Listener de ACKs iniciado<br><br>[DISCOVER #1] MAC: 02:a3:f1:22:bc:44<br><br>[DISCOVER #2] MAC: 02:7e:09:ab:31:cc<br><br>[ACK #1] IP asignada: 20.25.7.50<br><br>[ACK #2] IP asignada: 20.25.7.51<br><br>[*] DISCOVERs: 254 \| IPs consumidas: 254|

# 6. Funcionamiento del Ataque

Cada DHCP DISCOVER se envía con una MAC de origen diferente (generada aleatoriamente con bit unicast=0 y locally-administered=1). El servidor DHCP trata cada MAC como un cliente diferente y asigna una IP del pool a cada una. Cuando el pool se agota, el servidor responde con DHCP NAK a clientes legítimos o simplemente no responde.

•        Paso 1: Se genera una MAC aleatoria única para cada paquete.

•        Paso 2: Se construye DHCP DISCOVER con esa MAC en el campo chaddr de BOOTP.

•        Paso 3: Se envía a broadcast 255.255.255.255 puerto 67.

•        Paso 4: El servidor DHCP asigna una IP del pool a esa MAC falsa.

•        Paso 5: Se repite hasta agotar todas las IPs disponibles del pool.

•        Paso 6: Con --wait-ack se capturan los ACKs para registrar qué IPs fueron consumidas.

# 7. Verificación del Ataque

**Para confirmar que el ataque fue exitoso, se ejecutaron los siguientes comandos:**

Router# show ip dhcp binding

Router# show ip dhcp pool

Router# show ip dhcp conflict

|   |
|---|
|**¿Qué se debe observar?**<br><br>show ip dhcp binding muestra cientos de entradas con MACs falsas (02:xx:xx...).<br><br>show ip dhcp pool muestra Available = 0 (pool agotado).<br><br>Nuevos clientes no pueden obtener IP — reciben error de DHCP.|

# 8. Contramedidas

DHCP Snooping con rate limiting limita la cantidad de mensajes DHCP por segundo por puerto, evitando que un solo host pueda inundar el servidor con solicitudes.

Switch(config)# ip dhcp snooping

Switch(config)# ip dhcp snooping vlan 1

Switch(config-if)# ip dhcp snooping limit rate 15  ! Max 15 pkt/s por puerto

Router(config)# ip dhcp pool LAN  ! Reducir tamaño del pool al mínimo necesario

# 9. Conclusión

El DHCP Starvation es el precursor natural del DHCP Spoofing: primero se agota el pool legítimo y luego se levanta el servidor falso. La combinación de DHCP Snooping con rate limiting en los puertos de acceso es la defensa más efectiva contra este ataque.  
  
Link de GitHub: https://github.com/HeldryRoot/Ataque-DHCP-Starvation.git

**Heldry Terrero — Matrícula 2025-0719 — Seguridad de Redes — Junio 2026**
