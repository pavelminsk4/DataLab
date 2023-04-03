<template>
  <div class="users-icons-bar">
    <UserAvatar
      v-for="(item, index) in users.slice(0, numberDisplayedUsers)"
      :key="'photo' + index"
      :avatar-url="item?.user_profile.photo"
      :first-name="item.first_name"
      :last-name="item.last_name"
      :username="item.username"
    />

    <div v-if="users.length > numberDisplayedUsers" class="users-count">
      +{{ users.length - numberDisplayedUsers }}
    </div>
  </div>
</template>

<script>
import UserAvatar from '@components/UserAvatar'

export default {
  name: 'UsersIconsBar',
  components: {
    UserAvatar,
  },
  props: {
    users: {type: Array, required: true},
  },
  created() {
    this.numberDisplayedUsers = 3
  },
}
</script>

<style lang="scss" scoped>
.users-icons-bar {
  position: relative;

  display: flex;
  .users-count {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    flex-grow: 0;

    width: 22px;
    height: 22px;

    border-radius: 100%;

    font-style: normal;
    font-weight: 500;
    font-size: 10px;
    line-height: 10px;
    color: var(--typography-primary-color);
  }
}
</style>
