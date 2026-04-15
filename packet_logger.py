from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, ipv4, tcp, udp, icmp

log = core.getLogger()


def _handle_PacketIn(event):
    packet = event.parsed

    if not packet:
        return

    # Extract IP packet
    ip_packet = packet.find('ipv4')

    if ip_packet:
        src = ip_packet.srcip
        dst = ip_packet.dstip

        protocol = "UNKNOWN"

        if ip_packet.protocol == ipv4.TCP_PROTOCOL:
            protocol = "TCP"
        elif ip_packet.protocol == ipv4.UDP_PROTOCOL:
            protocol = "UDP"
        elif ip_packet.protocol == ipv4.ICMP_PROTOCOL:
            protocol = "ICMP"

        log.info("Packet: %s -> %s | Protocol: %s", src, dst, protocol)

    #  Forward packet (IMPORTANT FIX)
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Packet Logger Controller Started")
