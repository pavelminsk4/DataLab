<template>
  <div class="not-found-wrapper">
    <div class="error-description">
      <h2>Looks Like You Are Lost...</h2>
      <div class="hint">
        Sorry. The content you’re looking for doesn’t exist. Either it was
        removed, or you mistyped the link.
      </div>

      <BaseButton @click="goToHomepage">Go to Homepage</BaseButton>
    </div>

    <img src="@assets/404-error.svg" alt="404 Error" class="error-img" />
  </div>
</template>

<script>
import BaseButton from '@components/common/BaseButton'

export default {
  name: 'NotFoundPage',
  components: {
    BaseButton,
  },
  methods: {
    goToHomepage() {
      this.$router.push({
        name: 'MainView',
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.not-found-wrapper {
  display: flex;

  gap: 28px;
  margin: 80px 200px;

  .error-description {
    display: flex;
    flex-direction: column;
    flex: 1;

    .hint {
      margin: 32px 0 40px 0;
    }
  }

  .error-img {
    display: flex;
    flex: 1;
  }
}
</style>
