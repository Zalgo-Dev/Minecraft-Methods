Possible crash exploit via le plugin LoginSecurity 3.3.0.
Injection d'un uuid invalide dans le packet de connexion pour créer des connexions et saturer la mémoire du serveur.

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