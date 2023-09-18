<template>
  <TransitionGroup
    name="flash-messages"
    tag="div"
    class="flash-messages-container"
  >
    <template v-for="{id, title, message, type} in flashMessages" :key="id">
      <component :is="`${type}FlashMessage`" :title="title" @close="close(id)">
        {{ message }}
      </component>
    </template>
  </TransitionGroup>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import ErrorFlashMessage from '@components/flash-messages/ErrorFlashMessage'

export default {
  name: 'FlashMessagesContainer',
  components: {ErrorFlashMessage},
  computed: {
    ...mapState(['flashMessages']),
  },
  methods: {
    ...mapActions([action.CLOSE_FLASH_MESSAGE]),
    close(flashMessageId) {
      this[action.CLOSE_FLASH_MESSAGE](flashMessageId)
    },
  },
}
</script>

<style lang="scss" scoped>
.flash-messages-container {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 10;

  display: flex;
  flex-direction: column;
  gap: 15px;
}

.flash-messages-enter-active,
.flash-messages-leave-active {
  transition: all 0.5s ease;
}
.flash-messages-enter-from,
.flash-messages-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>
