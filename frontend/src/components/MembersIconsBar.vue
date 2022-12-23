<template>
  <div class="members-icons-bar">
    <img
      v-for="(item, index) in members.slice(0, 4)"
      :key="'photo' + index"
      :src="item?.user_profile.photo"
      :style="`z-index=${index + 1}`"
      class="member-icon"
    />

    <div v-if="members.length > 4" class="members-count">
      +{{ members.length - 4 }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'MembersIconsBar',
  props: {
    members: {type: Array, required: true},
  },
}
</script>

<style lang="scss" scoped>
.members-icons-bar {
  position: relative;

  display: flex;

  .member-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-grow: 0;
    flex-shrink: 0;

    width: 22px;
    height: 22px;

    border-radius: 100%;
    border: 1px solid var(--secondary-text-color);

    background-color: white;

    font-size: 10px;

    &:not(:first-child) {
      margin-left: -10px;
    }
  }

  .members-count {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    flex-grow: 0;

    width: 22px;
    height: 22px;
    margin-left: 8px;

    border-radius: 100%;
    border: 1px dashed var(--secondary-text-color);

    color: var(--secondary-text-color);

    font-style: normal;
    font-weight: 400;
    font-size: 10px;
    line-height: 20px;
  }
}
</style>
