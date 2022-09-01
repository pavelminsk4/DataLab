<template>
  <BaseModal>
    <h1>Add Workspace</h1>
    <h2>Title</h2>
    <BaseInput v-model="title" class="input" />
    <h2>Description</h2>
    <BaseInput v-model="description" class="input" />
    <BaseButton class="button" @click="addWorkspace">Add Workspace</BaseButton>
  </BaseModal>
</template>

<script>
import BaseInput from '@components/BaseInput'
import BaseModal from '@components/modals/BaseModal'
import BaseButton from '@components/buttons/BaseButton'

export default {
  name: 'NewWorkspaceModal',
  components: {
    BaseButton,
    BaseModal,
    BaseInput,
  },
  data() {
    return {
      loading: false,
      title: '',
      description: '',
    }
  },
  methods: {
    addWorkspace() {
      this.$emit('create-workspace', this.title, this.description)
    },
  },
}
</script>

<style scoped>
.input {
  margin-bottom: 20px;
}

.button {
  margin-bottom: 30px;
}
</style>
