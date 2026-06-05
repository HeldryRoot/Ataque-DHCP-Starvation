# Ataque-DHCP-Starvation

<img width="654" height="276" alt="image" src="https://github.com/user-attachments/assets/9e8e9b55-6e2a-4b3a-a7a4-246cedc2039f" />


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

Link del Video de Youtube: https://youtu.be/ofPDfktIVjM?si=A6VvtqI4Llbpp_Xz

**Heldry Terrero — Matrícula 2025-0719 — Seguridad de Redes — Junio 2026**
