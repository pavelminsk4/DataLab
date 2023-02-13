<template>
  <img
    v-if="haveAvatar"
    :src="avatarUrl"
    class="member-icon"
    @error="haveAvatar = false"
  />
  <div
    v-else
    :style="`--acronym-color: ${acronymColor}`"
    class="member-icon acronym"
  >
    {{ acronym }}
  </div>
</template>

<script>
import {PREDEFINED_COLORS} from '@/lib/constants'

export default {
  name: 'UserAvatar',
  props: {
    avatarUrl: {
      type: String,
      default: '',
    },
    firstName: {
      type: String,
      default: '',
    },
    lastName: {
      type: String,
      default: '',
    },
    username: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      haveAvatar: !!this.avatarUrl,
    }
  },
  computed: {
    acronym() {
      if (this.firstName && this.lastName) {
        return `${this.firstName[0]}${this.lastName[0]}`.toUpperCase()
      }
      return this.username[0].toUpperCase()
    },
    acronymColor() {
      const code =
        this.acronym.split().reduce((a, c) => a * c.charCodeAt(0), 1) %
        PREDEFINED_COLORS.length
      return PREDEFINED_COLORS[code]
    },
  },
}
</script>

<style lang="scss" scoped>
.member-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-grow: 0;
  flex-shrink: 0;

  width: 22px;
  height: 22px;

  border-radius: 50%;
  border: 1px solid var(--typography-secondary-color);

  background-color: white;

  font-weight: 500;
  font-size: 10px;
  line-height: 10px;
  color: var(--button-text-color);

  &:not(:last-child) {
    margin-right: 4px;
  }
}
.acronym {
  background-color: var(--acronym-color);
  border-color: var(--acronym-color);
}
</style>
