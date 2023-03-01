<template>
  <div class="blank-page-wrapper">
    <img :src="currentPage.src" :alt="currentPage.message" />
    {{ currentPage.message }} &#128542;
  </div>
</template>

<script>
export default {
  name: 'BlankPage',
  props: {
    pageName: {
      type: String,
      required: true,
    },
  },
  computed: {
    currentPage() {
      return this.pages[this.pageName]
    },
  },
  created() {
    this.pages = {
      OnlineWorkspaces: {
        src: require('@/assets/online-workspaces.png'),
        message: 'No workspaces created',
      },
      SocialMediaWorkspaces: {
        src: require('@/assets/social-media-workspaces.png'),
        message: 'No workspaces created',
      },
    }
  },
}
</script>

<style scoped>
.blank-page-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 35px;

  font-size: 18px;
}
</style>
