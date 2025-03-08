Possible Crash exploit by creating multiples fakes sessions. found by me in this shit plugin.
I make later.

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