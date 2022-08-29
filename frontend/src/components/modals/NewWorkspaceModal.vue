<template>
  <BaseModal>
    <h1>Add Workspace</h1>
    <h2>Title</h2>
    <BaseInput v-model="title" class="input"/>
    <h2>Description</h2>
    <BaseInput v-model="description" class="input"/>
    <BaseButton class="button" @click="createWorkspace">Add Workspace</BaseButton>
  </BaseModal>
</template>

<script>
import { mapActions } from 'vuex'
import { action } from '@store/constants'

import BaseInput from '@components/BaseInput'
import BaseModal from '@components/modals/BaseModal'
import BaseButton from '@components/buttons/BaseButton'

export default {
  name: "NewWorkspaceModal",
  components: {
    BaseButton,
    BaseModal, BaseInput
  },
  data() {
    return {
      loading: false,
      title: '',
      description: ''
    }
  },
  methods: {
    ...mapActions([action.CREATE_WORKSPACE]),
    async createWorkspace() {
      try {
        this.loading = true
        await this[action.CREATE_WORKSPACE]({
          title: this.title,
          description: this.description
        })
      } catch (error) {
        this.loading = false
      }
    },
  }
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