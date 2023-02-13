<template>
  <div class="members-icons-bar">
    <UserAvatar
      v-for="(item, index) in members.slice(0, numberDisplayedUsers)"
      :key="'photo' + index"
      :avatar-url="item?.user_profile.photo"
      :first-name="item.first_name"
      :last-name="item.last_name"
      :username="item.username"
    />

    <div v-if="members.length > numberDisplayedUsers" class="members-count">
      +{{ members.length - numberDisplayedUsers }}
    </div>
  </div>
</template>

<script>
import UserAvatar from '@components/UserAvatar'

export default {
  name: 'MembersIconsBar',
  components: {
    UserAvatar,
  },
  props: {
    members: {type: Array, required: true},
  },
  created() {
    this.numberDisplayedUsers = 3
  },
}
</script>

<style lang="scss" scoped>
.members-icons-bar {
  position: relative;

  display: flex;
  .members-count {
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
