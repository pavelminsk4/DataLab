<template>
  <BaseModal>
    <template #title>
      <span>Save as</span>
    </template>

    <section class="content">
      <img
        src="@assets/preset-created.png"
        alt="preset created image"
        class="image"
      />
      <p>
        You saved the <span>{{ presetName }}</span> preset to the
        <span>{{ groupName }}</span> group
      </p>
    </section>

    <footer class="footer">
      <BaseButton @click="$emit('close')">Done</BaseButton>
    </footer>
  </BaseModal>
</template>

<script>
import BaseButton from '@components/common/BaseButton'
import BaseModal from '@components/modals/BaseModal'

export default {
  name: 'PresetCreatedModal',
  components: {
    BaseButton,
    BaseModal,
  },
  props: {
    presetName: {type: String, default: ''},
    groupName: {type: String, default: ''},
  },
}
</script>

<style lang="scss" scoped>
.content {
  display: flex;
  flex-direction: column;
  gap: 24px;
  align-items: center;

  min-width: 455px;
  margin-bottom: 32px;
}

.footer {
  display: flex;
  justify-content: flex-end;

  width: 100%;

  background-color: var(--background-secondary-color);
}

.image {
  width: 315px;
}
</style>
