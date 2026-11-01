# 62. Design a video conferencing system (Zoom/Meet).

> Part B: Classic System Designs

**Answer:** Signaling server (WebSocket) for session setup (SDP/ICE), WebRTC media; 1:1 P2P, groups use SFU (selective forwarding; scalable) vs MCU (mixing; heavy). TURN for NAT traversal, simulcast/adaptive bitrate, regional media servers.

```
A --\
B ---> [SFU] --> subscribers     (signaling via WS)
C --/
```

---
[⬆ Back to index](../../README.md#-question-index)
