Possible crash exploit via le plugin LoginSecurity 3.3.0

## Vulnerable Code:
```
public final PlayerSession getPlayerSession(final Player player) {
        final UUID userId = ProfileUtil.getUUID(player);
        final PlayerSession session;
        if(activeSessions.containsKey(userId)) {
            session = activeSessions.get(userId);
        } else {
            session = preloadCache.getUnchecked(userId);
            if(player.isOnline()) {
                activeSessions.put(userId, session);
                preloadCache.invalidate(userId);
            }
        }

        return session;
    }
```