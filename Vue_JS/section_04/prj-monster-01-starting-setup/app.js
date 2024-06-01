function getRandomValue(min, max) {
  return Math.random() * (max - min) + min;
}

Vue.createApp({
  data() {
    return {
      playerHealth: 100,
      monsterHealth: 100,
      currentRound: 1,
      winner: null,
      battleLogs: []
    };
  },
  watch: {
    currentRound() {
      console.log('call currentRound');
      this.checkWinner();
    },
    playerHealth(value) {
      console.log('call playerHealth');
      if (value > 100) this.playerHealth = 100;
    },
    monsterHealth(value) {
      console.log('call monsterHealth');
    }
  },
  computed: {
    monsterHealthBarStyles() {
      console.log('call monsterHealthBarStyles');
      if (this.monsterHealth < 0) {
        return { width: 0 + '%' };
      }
      return { width: this.monsterHealth + '%' };
    },
    playerHealthBarStyles() {
      console.log('call playerHealthBarStyles');
      if (this.playerHealth < 0) {
        return { width: 0 + '%' };
      }
      return { width: this.playerHealth + '%' };
    },
    specialAttackStatus() {
      console.log('call specialAttackStatus');
      return this.currentRound % 3 != 0;
    }
  },
  methods: {
    attackMonster() {
      const attackValue = getRandomValue(5, 12);
      this.monsterHealth -= attackValue;
      this.insertBattleLog('player', 'attack', attackValue);
      this.attackPlayer();
      this.currentRound++;
    },
    attackPlayer() {
      const attackValue = getRandomValue(8, 15);
      this.playerHealth -= attackValue;
      this.insertBattleLog('monster', 'attack', attackValue);
    },
    specialAttack() {
      const attackValue = getRandomValue(10, 25);
      this.monsterHealth -= attackValue;
      this.insertBattleLog('player', 'attack', attackValue);
      this.attackPlayer();
      this.currentRound++;
    },
    playerHeal() {
      const healValue = getRandomValue(8, 25);
      this.playerHealth += healValue;
      this.insertBattleLog('player', 'heal', healValue);
      this.attackPlayer();
      this.currentRound++;
    },
    checkWinner() {
      if (this.playerHealth <= 0 && this.monsterHealth <= 0) {
        this.winner = 'draw';
      } else if (this.playerHealth <= 0) {
        this.winner = 'monster';
      } else if (this.monsterHealth <= 0) {
        this.winner = 'player';
      }
    },
    startGame() {
      this.playerHealth = 100;
      this.monsterHealth = 100;
      this.currentRound = 1;
      this.winner = null;
      this.battleLogs = [];
    },
    surrender() {
      this.winner = 'monster';
    },
    insertBattleLog(who, what, value) {
      const battleLog = {
        actionBy: who,
        actionType: what,
        actionValue: Math.floor(value)
      };
      this.battleLogs.unshift(battleLog);
    }
  }
}).mount('#game');
