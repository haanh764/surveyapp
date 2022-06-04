<template>
  <v-list
    expand
    nav
    v-bind="$attrs"
    v-on="$listeners"
  >
    <template v-for="(item, i) in items">
      <default-list-group
        v-if="item.items"
        :key="`group-${i}`"
        :item="item"
      />

      <default-list-item
        v-else
        :key="`item-${i}`"
        class="default-list-item"
        :class="{'--is-last-before-separation': item.isLastBeforeSeparation}"
        :item="item"
      />
      <v-divider
        v-if="item.isLastBeforeSeparation"
        :key="`divider-${i}`"
        class="mx-3 mb-2"
      />
    </template>
  </v-list>
</template>

<script>
export default {
  name: "DefaultList",

  components: {
    DefaultListGroup: () => import("./ListGroup"),
    DefaultListItem: () => import("./ListItem")
  },

  props: {
    items: {
      type: Array,
      default: () => ([])
    }
  }
};
</script>

<style lang="scss">

.default-list-item {
  &.--is-last-before-separation {
    margin-bottom: 80px !important;
  }
}
</style>
